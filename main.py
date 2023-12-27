import logging
import os
from pathlib import Path

from app.config.config import ecu_to_dict
from app.context import Constant, Profile
from app.entry import StudioApp
from foundation.force.concurrent import Threading
from log.log import init_logging

logger = logging.getLogger(__name__)


def main():
    import harbour
    harbour.EcuInfo = ecu_to_dict()
    init_logging()
    logger.info('run studio')
    Threading().start()
    app: StudioApp = StudioApp()
    app.run()
    Threading().terminate()
    logger.info('stop studio')


if __name__ == "__main__":
    root_path: str = os.path.dirname(__file__)
    Profile().put(Constant.cApp_Root_Path, root_path)
    Profile().put(Constant.cApp_Config_Path, str(Path(root_path).joinpath('config')))
    Profile().put(Constant.cApp_Assets_Path, str(Path(root_path).joinpath('assets')))
    Profile().put(Constant.cApp_Assets_Icon_Path, str(Path(root_path).joinpath('assets').joinpath('icon')))
    # Profile().put(Constant.cApp_Language_Path, str(Path(root_path).joinpath('language')))
    main()
