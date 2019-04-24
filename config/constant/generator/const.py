class GeneratorConsts:
    DIRECTION_BUY = "buy"
    DIRECTION_SELL = "sell"
    DIRECTIONS = (DIRECTION_BUY, DIRECTION_SELL)

    STATUS_NEW = "new"
    STATUS_TO_PROVIDER = "to provider"
    STATUS_REJECT = "reject"
    STATUS_FILLED = "filled"
    STATUS_PARTIAL_FILLED = "partial filled"
    STATUSES = (STATUS_NEW, STATUS_TO_PROVIDER, STATUS_REJECT, STATUS_FILLED, STATUS_PARTIAL_FILLED)
    FINAL_STATUSES = (STATUS_REJECT, STATUS_FILLED, STATUS_PARTIAL_FILLED)

    RED_ZONE = "red"
    GREEN_ZONE = "green"
    BLUE_ZONE = "blue"

    ZONES = (RED_ZONE, GREEN_ZONE, BLUE_ZONE)

    WEEK_TIMESTAMP = 604800000
