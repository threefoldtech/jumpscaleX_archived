TradingIsClosedError = "-5" # Trading session is closed
OrderAlreadyProcessed = "-6" # Request order is already processed
NotEnoughMoneyError = "-2" # Not enough money to make a position
PositionClosedError = "-10" # Position is already closed.
CannotHedgeError = "-4" # Hedging is not allowed
PositionInPendingModeError = "-11" # Position in pending mode
MarketConditionError = "-50" # Market condition violated
BadConnectionError = "-51" # Bad connection
InternalError = "-200" # Web Service internal error
LoginRequiredError = "-201" # Login is required
InvalidAccountError = "-202" # Invalid account identifier or account is not accessible by logged in client
InvalidTicketError = "-203" # Invalid ticket identifier or ticket is not accessible by logged in client
InvalidOrderError = "-204" # Invalid order identifier or order is not accessible by logged in client
InvalidAmountError = "-205" # Invalid amount
InvalidCloseByHedgeError = "-206" # Error closing given tickets with each other
InvalidLoginInfoUsernameError = "-207" # Invalid username
InvalidLoginInfoPasswordError = "-1" # invalid password
SymbolNotFoundError = "-208" # Invalid symbol name or identifier
InvalidDateFormatError = "-209" # Date format must be in DD/MM/YYYY format
NoDateFoundError = "-210" # No data found for given identifier
InvalidOrderTypeEror = "-211" # Order type is not buy neither sell
CancelLimitOrderError = "-212" # Could not delete limit order
DeleteSLTPOrderError = "-213" # Could not delete SLTP order
UpdateSLTPError = "-214" # Couldn't update SLTP order
NewLimitOrderError = "-215" # Couldn’t place limit order
UpdateLimitOrderError = "-216" # Couldn’t update limit order
LimitOrderNotFoundError = "-217" # Limit order not exist or processed
LimitOrderDeletedExecutedError = "-218" # Limit order not exist or processed
IsReadOnlyError = "-219" # Account is readonly, cannot trade
IsLockedError = "-220" # Account is locked, cannot trade
SendingMailError = "-221" # Could not send mail to department
SendMailInvalidUserError = "-222" # Invalid user /sending failure
JustCloseSymbol = "-223" # Symbol is in just close only
BuyOnlySymbol = "-224" # Symbol in buy mode only
DateISNotLogical = "-225" # Not logical date
InvalidDepositAmountError = "-226" # Deposit amount is not valid
MarketOrderNotFound = "-229" # Invalid  order" # ID
InvalidOrMissingParametersError = "-227" # Missing parameters invalid given value.
InvalidPrice = "-228" # Invalid price value.
AllLotsAreManaged = "-230" # Open managed order with a position previously had managed at the overall amount.
NoAccount = "-231" # Login with a client does not have an account.
InvalidLogin = "-232" # Not valid login .
InvalidOperationType = "-233" # Not valid money trans type.
InvalidSerial = "-235" # Enter invalid serial.
HedgeingNotAllowed = "-248" # When hedging not allowed.
InvalidUsername = "-240" # Create client with used client username.
NoPrivilege = "-241" # When making an operation the dealer does not have a privilege on it
InvalidClientID = "-242" # When passing invalid client id.
PositionIsClosed = "-243" # When making an operation on the position already closed
PositionHasSLTP = "-244" # When making an operation on the position has SLTP.
AlreadyProcessed = "-246" # When making an operation on the position that already processed.
DataBaseError = "-247" # unexpected database error
NoData = "-1000" # Request returned 0 data in list
IsPaging = "-1200" # GetHistory operation has returned more than 3000 rows and so you’ll need to call it with isPaging=true to retrieve remaning rows
PositionIsFreezed = "-236" # When making any operation on the freezed position
InvalidNewOldSamePassword = "-237" # When changing password and the old password is the same of the new password
InvalidOldPassword = "-239" # When changing password and old password is invalid
InvalidPassword = "-238" # When enter invalid password
InvalidDeliveryPrice = "-249" # When enter invalid price for delivery
InvalidPeriodID = "-251" # When enter invalid period for chart function
