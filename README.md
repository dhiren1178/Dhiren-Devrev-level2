# Dhiren-Devrev-level2
Flight Ticket Booking Use Case Backend
# Flight Ticket Booking Application

This is a web application for flight ticket booking. Users can search for flights, make bookings, and admins can manage flights and view bookings.

## Features

- User Registration and Authentication: Users can sign up and log in to access their account and make bookings.
- Flight Search: Users can search for flights based on origin, destination, departure date, and time.
- Flight Booking: Users can book tickets for available flights and select preferred seats.
- My Bookings: Users can view their booking history, including upcoming and past flights.
- Admin Dashboard: Admin users have access to a dashboard for managing flights and viewing bookings.

## Technologies Used

- Python
- Django Framework
- HTML
- CSS

## Setup and Installation

1. Clone the repository:

```bash
git clone https://github.com/dhiren1178/Dhiren-Devrev-level2
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Change to the project directory:

```bash
cd DevRev-Flight-Ticket-Booking/
```

4. Run the database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Access the application in your web browser at `http://localhost:8000`.

7. Admin Login Details:

   - Username: admin
   - Password: admin123

8. User Login Details:

   - Username: sampleuser
   - Password: user@123

9. Available Flight Lists:

- Flight Number: DLE44567, Airline: Air India, From: Delhi, To: Mumbai, Departure Date & Time: July 13, 2023, 14:45:00
- Flight Number: 3458398, Airline: Jet Airways, From: Madurai, To: Chennai, Departure Date & Time: July 14, 2023, 12:45:00
- Flight Number: 3458398, Airline: IndiGo, From: Delhi, To: London, Departure Date & Time: July 15, 2023, 18:50:00
- Flight Number: EF890651, Airline: British Airways, From: Delhi, To: Sandtoft, Departure Date & Time: July 18, 2023, 03:00:00
- Flight Number: LB593089E, Airline: American Airlines, From: Denver, To: Mumbai, Departure Date & Time: July 20, 2023, 23:00:00

Please note that this information is based on the provided details, and you may need to modify it based on your specific project setup.
