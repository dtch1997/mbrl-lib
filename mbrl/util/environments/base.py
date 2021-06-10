import mbrl


class UnsupportedEnvironmentException(RuntimeError):
    """Raise this exception if your constructor does not support creating the environment"""
    pass

class MBRLCompatEnv():
    def __init__(self, cfg):
        self.term_fn : mbrl.types.TermFnType
        self.reward_fn : mbrl.types.RewardFnType,

        raise NotImplementedError(f"No environment found for `{cfg.override.env}`.")
