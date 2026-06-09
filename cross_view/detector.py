class CrossViewDetector:

    @staticmethod
    def compare(memory_view, os_view):

        os_pids = {process.pid for process in os_view}

        hidden = []

        for process in memory_view:

            if process.pid not in os_pids:
                hidden.append(process)

        return hidden