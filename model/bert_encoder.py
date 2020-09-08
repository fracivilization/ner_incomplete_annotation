from model.bilstm_encoder import BiLSTMEncoder

class BERTEncoder(BiLSTMEncoder):
    def __init__(self, config, print_info: bool = True):
        super().__init__(config, print_info= True)
