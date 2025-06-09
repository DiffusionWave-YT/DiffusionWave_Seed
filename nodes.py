import nodes
import torch
import comfy.model_management


MAX_SEED_NUM=999999999999

class Seed__DiffusionWave:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "seed": ("INT", {"default": 0, "min": 0, "max": MAX_SEED_NUM}),
            },
            "hidden": {"prompt": "PROMPT", "extra_pnginfo": "EXTRA_PNGINFO", "my_unique_id": "UNIQUE_ID"},
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("seed",)    
    FUNCTION = "Seed__DiffusionWave_FUNC"
    CATEGORY = "Seed"

    def Seed__DiffusionWave_FUNC(self, seed=0, prompt=None, extra_pnginfo=None, my_unique_id=None):
        return seed,



NODE_CLASS_MAPPINGS = {
    "Seed__DiffusionWave 🌊": Seed__DiffusionWave,
}


