import json

# Database to store trade fair details
trade_fairs_db = []

# Function to add a new trade fair
def add_trade_fair():
    name = input("Enter the name of the trade fair: ")
    date = input("Enter the date (YYYY-MM-DD)-(YYYY-MM-DD): ")
    location = input("Enter the location: ")
    tickets_available = int(input("Enter the number of available tickets: "))
    ticket_price = float(input("Enter the ticket price: $"))
    
    trade_fair = {
        "name": name,
        "date": date,
        "location": location,
        "tickets_available": tickets_available,
        "ticket_price": ticket_price
    }
    
    trade_fairs_db.append(trade_fair)
    print(f"{name} trade fair added successfully.")

# Function to list available trade fairs
def list_trade_fairs():
    if not trade_fairs_db:
        print("No trade fairs available.")
    else:
        print("\nAvailable Trade Fairs:")
        for i, trade_fair in enumerate(trade_fairs_db, start=1):
            print(f"{i}. {trade_fair['name']} ({trade_fair['date']}) - {trade_fair['location']}")

# Function to book tickets for a trade fair
def book_ticket():
    list_trade_fairs()
    if not trade_fairs_db:
        return
    
    try:
        choice = int(input("Enter the number of the trade fair you want to book tickets for: "))
        if 1 <= choice <= len(trade_fairs_db):
            trade_fair = trade_fairs_db[choice - 1]
            print(f"Booking for {trade_fair['name']} ({trade_fair['date']})")
            
            tickets_requested = int(input("Enter the number of tickets you want to book: "))
            if tickets_requested > trade_fair['tickets_available']:
                print("Sorry, there are not enough tickets available.")
            else:
                total_cost = tickets_requested * trade_fair['ticket_price']
                print(f"Total cost: ${total_cost}")
                confirm = input("Confirm booking (yes/no): ").lower()
                if confirm == "yes":
                    trade_fair['tickets_available'] -= tickets_requested
                    print(f"Booking confirmed for {tickets_requested} tickets.")
                else:
                    print("Booking canceled.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid choice.")

# Main menu
while True:
    print("\nTrade Fair Booking System")
    print("1. Add Trade Fair")
    print("2. List Available Trade Fairs")
    print("3. Book Tickets")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_trade_fair()
    elif choice == "2":
        list_trade_fairs()
    elif choice == "3":
        book_ticket()
    elif choice == "4":
        print("Exiting the Trade Fair Booking System.")
        break
    else:
        print("Invalid choice. Please select a valid option.")


from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Dummy list to store bookings (in a real application, use a database)
bookings = []

# Replace with your actual payment gateway integration
def process_payment(booking_id, amount):
    # Simulate a payment transaction here
    # In a real application, use a payment gateway like Stripe, PayPal, etc.
    return True

@app.route('/', methods=['GET', 'POST'])
def book_trade_fair():
    if request.method == 'POST':
        trade_fair = request.form.get('trade_fair')
        booth_type = request.form.get('booth_type')
        num_booths = int(request.form.get('num_booths'))
        amount = num_booths * 500  # Replace with your pricing logic

        # Simulate payment processing
        if process_payment(len(bookings) + 1, amount):
            bookings.append({
                'trade_fair': trade_fair,
                'booth_type': booth_type,
                'num_booths': num_booths,
                'amount': amount
            })

            return redirect(url_for('success'))

    return render_template('booking.html')

@app.route('/success')
def success():
    return "Booking successful!"

if __name__ == '__main__':
    app.run(debug=True)
