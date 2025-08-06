
EXPERIMENT_CONFIGS = {
    # Experiment 1: 6 Matern kernels with rank 1
    "lcm_6matern_rank1": {
        "model_class": "LCM6MaternRank1Model",
        "params": {},
        "description": "LCM with 6 Matern kernels (nu=0.5) and rank 1"
    },
    
    # Experiment 2: 1 Matern kernel with rank 6
    "lcm_1matern_rank6": {
        "model_class": "LCM1MaternRank6Model",
        "params": {},
        "description": "LCM with 1 Matern kernel (nu=0.5) and rank 6"
    },
    
    # Experiment 3: 2 Matern kernels with rank 3
    "lcm_2matern_rank3": {
        "model_class": "LCM2MaternRank3Model",
        "params": {},
        "description": "LCM with 2 Matern kernels (nu=0.5) and rank 3"
    }
}