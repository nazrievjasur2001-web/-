"""Safe Solana trading-bot scaffold. Paper trading only; no live orders."""
from __future__ import annotations

import logging
import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger("solana-ai-trader")


@dataclass(frozen=True)
class Settings:
    trading_mode: str = os.getenv("TRADING_MODE", "paper").lower()
    max_trade_usd: float = float(os.getenv("MAX_TRADE_USD", "10"))
    max_daily_loss_usd: float = float(os.getenv("MAX_DAILY_LOSS_USD", "20"))


def validate(settings: Settings) -> None:
    if settings.trading_mode != "paper":
        raise RuntimeError("Live trading is not implemented. Keep TRADING_MODE=paper.")
    if settings.max_trade_usd <= 0 or settings.max_daily_loss_usd <= 0:
        raise ValueError("Risk limits must be positive.")


def main() -> None:
    settings = Settings()
    validate(settings)
    log.info("Solana AI Trader scaffold started in PAPER mode.")
    log.info("Risk limits: max trade=$%.2f; max daily loss=$%.2f",
             settings.max_trade_usd, settings.max_daily_loss_usd)
    log.info("No wallet connected. No real transactions will be sent.")


if __name__ == "__main__":
    main()
