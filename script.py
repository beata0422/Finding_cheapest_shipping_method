def ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 + (price_per_pound * weight)
print(ground_shipping(8.4))

premium_ground_shipping = 125

def drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 14.00
  else:
    price_per_pound = 14.25
  return price_per_pound * weight
print(drone_shipping(1.5))

def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  premium = premium_shipping
  drone = drone_shipping(weight)

  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < done:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone

  print(
    "The cheapest option available costs $%.2f with s% shipping"
    % (cost, method))

print(cheapest_shipping(4.8))
print(cheapest_shipping(41.5))