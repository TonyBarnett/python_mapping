class Classifier:
    """ The base class for a classifier, each method must be overridden (hence all the notImplementedErrors)
    """
    def __init__(self):
        self.name = None

    def train(self, training_documents):
        raise NotImplementedError()

    def run_items(self, validation_documents):
        raise NotImplementedError()

    def get_result_for_item(self, item_id=None):
        raise NotImplementedError()

    def __str__(self):
        return self.name