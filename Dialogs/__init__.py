from aiogram import Router
import Dialogs.Start

router = Router()
router.include_routers(Start.router)
