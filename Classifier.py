class Classifier:
    """ The base class for a classifier, each method must be overridden (hence all the notImplementedErrors)
    """
    def __init__(self, name):
        self.name = name
        self.classes = list()

    def train(self, training_documents: list):
        raise NotImplementedError()

    def run_items(self, validation_documents: list):
        raise NotImplementedError()

    def get_result_for_item(self, item_id=None):
        raise NotImplementedError()

    def __str__(self):
        return self.name