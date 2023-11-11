from models import *
import hydra
from omegaconf import DictConfig, OmegaConf
from data_modules import *


@hydra.main(config_path="../cfg", config_name="trainer")
def main(cfg: DictConfig) -> None:
    model = MaximumLikelihood()
    # Init data module instance
    data_module = OnlineModule() if cfg.train_mode == "online" else OfflineModule()

    # Start fitting
    model.fit(data_module)


if __name__ == "__main__":
    main()
