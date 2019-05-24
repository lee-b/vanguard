from straight.plugin import load as _load_plugins


class Plugin:
    @classmethod
    def load_plugins(cls, module_path_str, base_class=None):
        if base_class is None:
            base_class = cls

        return _load_plugins(module_path_str, base_class)
