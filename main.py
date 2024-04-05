import sys
import numpy as np
import pandas as pd

# colspecs = [
# (1, 25, 'File ID')
# , (1, 3, '`File Type'), (3, 9, '`File Reference Date'), (9, 19, '`Processor ID'), (19, 25, '`File Sequence Number')
# , (25, 25+8, 'Message Number (DE71)')
# , (34, 34+19, 'Claim ID')
# , (53, 53+19, 'Event ID')
# , (72, 72+10, 'Cycle ID (DE95)')
# , (82, 82+23, 'Acquirer Reference Number (DE31)')
# ]
# colspecs0based = []
# for col in colspecs:
#     colspecs0based.append( (col[0] - 1, col[1] - 1 ) )
# colspecsNames = []
# for col in colspecs:
#     colspecsNames.append(col[2])
# df = pd.read_fwf('YTF.AR.TQR6.S.E0098531.D240321.T182740.A001.positional', colspecs=colspecs0based, names=colspecsNames)


widthsSpec = [
(25, 'File ID')
, (8, 'Message Number (DE71)')
, (19, 'Claim ID')
, (19, 'Event ID')
, (10, 'Cycle ID (DE95)')
, (23, 'Acquirer Reference Number (DE31)')

, (4, 'MTI')
, (19, 'Primary Account Number')
, (6, 'Processing Code')
, (3, 'Function Code')
, (4, 'Message Reason Code')
, (12, 'Amount Transaction')
, (12, 'Amount Reconciliation')

, (12, 'Amount Cardholder Billing')
, (3, 'Transaction Currency Code')
, (3, 'Reconciliation Currency Code')
, (3, 'Cardholder Billing Currency code')
, (4, 'Transaction Currency code and exponent')
, (4, 'Reconciliation Currency code and exponent')
, (4, 'Cardholder Billing Currency code and exponent')
# this is UI and API only fields.
# , (1, 'Transaction Currency exponent')
# , (1, 'Reconciliation Currency exponent')
# , (1, 'Cardholder Billing Currency exponent')

, (12, 'Retrieval Reference Number')
, (4, 'Card Acceptor Business Code')
, (15, 'Card Acceptor ID')
, (22, 'Card AcceptorName')
, (12, 'Date & Time of Transaction')
, (11, 'Transaction Originator Institution ID Code')
, (11, 'Transaction Destination Institution ID Code')
, (7, 'Transaction Status')

, (512, 'Reason for Rejection')
, (1, 'Reversal Flag')
]


widths = []
for tupl in widthsSpec:
    widths.append(tupl[0])
widthsNames = []
for tupl in widthsSpec:
    widthsNames.append(tupl[1])

#converters={i: str for i in range(len(widthsNames))}
#print(converters)

df = pd.read_fwf(sys.argv[1], widths=widths,
   names=widthsNames, keep_default_na=False, converters={i: str for i in range(len(widthsNames))})

print(df.transpose())
#df.to_csv(sys.argv[1] + '.csv')
