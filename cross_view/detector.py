class CrossViewDetector:

    @staticmethod
    def compare(view_a, view_b):

        hidden = []

        for item in view_a:
            if item not in view_b:
                hidden.append(item)

        return hidden