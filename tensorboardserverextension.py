from subprocess import Popen


def load_jupyter_server_extension(nbapp):
    """serve the tensorboard with data from logs directory"""
    Popen(["tensorboard", "--logdir", "logs", "--port", "6006"])
