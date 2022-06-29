logistic_status_choices = (
    ("Received", "Received"),
    ("In Transit", "In Transit"),
    ("Delivered", "Delivered"),
    ("Wrong Delivery Address", "Wrong Delivery Address"),
    ("Unable to Locate Address", "Unable to Locate Address"),
    ("Unable to Contact Receiver", "Unable to Contact Receiver"),
)

shipping_status_choices = (
    ("Received", "Received"),
    ("In Transit", "In Transit"),
    ("Delivered", "Delivered"),
    ("Shipment undergoing US customs routine inspection", "Shipment undergoing US customs routine inspection",),
    ("Shipment undergoing UK customs routine inspection", "Shipment undergoing UK customs routine inspection"),
    ("Shipment undergoing CA customs routine inspection", "Shipment undergoing CA customs routine inspection"),
    ("Shipment is now in transit to Lagos, Nigeria", "Shipment is now in transit to Lagos, Nigeria"),
    ("Shipment held by US custom please provide purchase receipt", "Shipment held by US custom please provide purchase receipt"),
    ("Shipment  held by UK custom please provide purchase receipt", "Shipment  held by UK custom please provide purchase receipt"),
    ("Shipment available for pick up please request for delivery", "Shipment available for pick up please request for delivery"),
    ("Good held by US custom, undergoing further investigation", "Good held by US custom, undergoing further investigation")
)

shipping_payment_choices = (
    ("Paid", "Paid"),
    ("Unpaid", "Unpaid")
)