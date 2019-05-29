def computepay(h,r):
    gr_p = h * r
    return gr_p

hrs = input("Enter Hours:")
rph = input("Enter Rate:")
fh = float(hrs)
fr = float(rph)
if fh > 40:
    common_pay = computepay(40,fr)
    extra_pay = computepay(fh - 40,fr * 1.5)
    p = common_pay + extra_pay
else:
    p = computepay(fh,fr)
print("Pay",p)
