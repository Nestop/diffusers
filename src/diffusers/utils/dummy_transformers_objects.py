# This file is autogenerated by the command `make fix-copies`, do not edit.
# flake8: noqa
from ..utils import DummyObject, requires_backends


class GlideSuperResUNetModel(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])


class GlideTextToImageUNetModel(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])


class GlideUNetModel(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])


class UNetGradTTSModel(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])


class Glide(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])


class LatentDiffusion(metaclass=DummyObject):
    _backends = ["transformers"]

    def __init__(self, *args, **kwargs):
        requires_backends(self, ["transformers"])