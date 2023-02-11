from torch import nn, optim

models_registry = {}

criterions_registry = {
    'bce': nn.BCELoss,
    'nll': nn.NLLLoss,
    'cross_entropy': nn.CrossEntropyLoss,
    'mse': nn.MSELoss,
    'ctc': nn.CTCLoss
}

optimizers_registry = {
    'adam': optim.Adam,
    'adamw': optim.AdamW,
    'sgd': optim.SGD
}

lr_schedulers_registry = {
    'reduce_on_plateau': optim.lr_scheduler.ReduceLROnPlateau,
    'cosine_lr': optim.lr_scheduler.CosineAnnealingLR
}


def build_model(name: str, config=None, **kwargs):
    """
    Build the model using its registry name. If config is None then the model is built using the default config. Notice
    that this function only builds the model and does not perform any weights loading/initialization unless these
    actions are done in the model's `.build()` method.

    Args:
        name (str): name of the model in the models' registry
        config (ModelConfig): a ModelConfig instance
        kwargs: extra config parameters that are loaded to the model

    Returns:
        A Model instance
    """

    config = config or models_registry[name]['model_config']()
    model = models_registry[name]['model_class'](config, **kwargs)
    return model


def build_criterion(name, config=None):
    """
        Build the loss function using its registry name.

        Args:
            name (str): Name of the optimizer in the criterions_registry
            config (CriterionConfig): A CriterionConfig  instance

        Returns:
            An nn.Module instance
        """
    criterion = criterions_registry[name](**config)
    return criterion


def build_optimizer(name, params, config=None):
    """
    Build the optimizer using its registry name.

    Args:
        name (str): Name of the optimizer in the optimizers_registry
        params (Iterator[nn.Parameter]): Model parameters
        config (OptimizerConfig): An OptimizerConfig  instance

    Returns:
        An optim.Optimizer instance
    """
    optimizer = optimizers_registry[name](params, **config)
    return optimizer


def build_scheduler(name, optimizer, config=None):
    """
        Build the LR scheduler using its registry name.

        Args:
            name (str): Name of the optimizer in the lr_schedulers_registry
            optimizer (optim.Optimizer): The optimizer
            config (OptimizerConfig): An LRSchedulerConfig  instance

        Returns:
            An optim.lr_scheduler._LRScheduler instance
        """
    scheduler = lr_schedulers_registry[name](optimizer, **config)
    return scheduler
