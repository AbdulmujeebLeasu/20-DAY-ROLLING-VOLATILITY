rm(list = ls())
dev.off()
cat("\014")



required_packages <- c("quantmod", "dplyr", "zoo")
missing_packages <- required_packages[!sapply(required_packages, requireNamespace, quietly = TRUE)]
if (length(missing_packages) > 0) {
  install.packages(missing_packages)
}

library(quantmod)
library(dplyr)
library(zoo)


SYMBOL              <- toupper(trimws(readline(prompt = "What Ticker (char): ")))
LOOKBACK_PERIOD     <- 365
VOL_WINDOW          <- 20
TRADING_DAYS_PER_YEAR <- 252

if (SYMBOL == "") stop("No ticker symbol entered.")

prices <- tryCatch(
  getSymbols(
    SYMBOL,
    src         = "yahoo",
    from        = Sys.Date() - LOOKBACK_PERIOD,
    to          = Sys.Date(),
    auto.assign = FALSE
  ),
  error = function(e) stop(sprintf("Failed to download '%s': %s", SYMBOL, e$message))
)

adjusted_col <- paste0(SYMBOL, ".Adjusted")
adjusted_prices <- prices[, adjusted_col]



close_returns <- periodReturn(
  adjusted_prices,
  period  = "daily",
  type    = "log",
  leading = TRUE
)

rolling_vol <- rollapply(
  close_returns[, "daily.returns"],
  width = VOL_WINDOW,
  FUN   = sd,
  align = "right"
)

annualized_rolling_vol <- rolling_vol * sqrt(TRADING_DAYS_PER_YEAR)



df <- bind_cols(
  adjusted_prices,
  close_returns,
  rolling_vol,
  annualized_rolling_vol
) %>%
  rename(
    Adjusted_Prices      = 1,
    Close_Returns        = 2,
    Volatility           = 3,
    Annualized_Volatility = 4
  )

result <- na.omit(df)

result
