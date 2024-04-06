
import qrcode
import matplotlib.pyplot as plt

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    qr_code = qr.make_image(fill_color="black", back_color="orange")

    plt.imshow(qr_code, cmap="gray")
    plt.axis("off")
    plt.show()

def generate_link_qr():
    link = input("Enter the link: ")
    generate_qr_code(link)

def generate_upi_qr():
    upi_id = input("Enter the UPI ID: ")
    upi_link = f"upi://pay?pa={upi_id}"
    generate_qr_code(upi_link)

def generate_gmail_qr():
    email = input("Enter the Gmail address: ")
    mailto_link = f"mailto:{email}"
    generate_qr_code(mailto_link)

def generate_telephone_qr():
    telephone = input("Enter the telephone number: ")
    tel_link = f"tel:{telephone}"
    generate_qr_code(tel_link)

def generate_qr_code_menu():
    print("Please select an option:")
    print("1. Generate QR code for a link")
    print("2. Generate QR code for a UPI ID")
    print("3. Generate QR code for a Gmail address")
    print("4. Generate QR code for a telephone number")
    option = input("Enter your choice  from (1-4): ")
    if option == "1":
        generate_link_qr()
    elif option == "2":
        generate_upi_qr()
    elif option == "3":
        generate_gmail_qr()
    elif option == "4":
        generate_telephone_qr()
    else:
        print("Invalid option!")

# Main program
generate_qr_code_menu()
