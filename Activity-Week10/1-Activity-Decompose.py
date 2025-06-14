# Decompose the following function and share your results via a GitHub link. See the function below:
'''
import datetime
 
def log_event(event_type, user_id, message):
    """Logs an event to a file with timestamp, event type, user ID, and message."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] [{event_type}] User: {user_id} - {message}\n"
    with open("rental_log.txt", "a") as log_file:
        log_file.write(log_message)
'''
import datetime


def get_timestamp():
    """Returns the current timestamp"""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def format_log_message(event_type, user_id, message):
    """Formats the log message with a timestamp, event type, user ID, and message"""
    timestamp = get_timestamp()
    return f"[{timestamp}] [{event_type}] User: {user_id} - {message}\n"


def write_to_log_file(log_message, file_name="rental_log.txt"):
    """Appends the log message to the specified file"""
    with open(file_name, "a") as log_file:
        log_file.write(log_message)


def log_event(event_type, user_id, message):
    """Logs an event by formatting and writing it to a file"""
    log_message = format_log_message(event_type, user_id, message)
    write_to_log_file(log_message)


# Add a main function to make it executable
def main():
    """Main function to demonstrate the logging functionality"""
    print("Rental Logger - Testing functionality")

    # Example usage
    log_event("LOGIN", "user123", "User logged into the system")
    log_event("RENTAL", "user123", "Rented car ID: CAR456")
    log_event("RETURN", "user123", "Returned car ID: CAR456")

    print("Log entries have been written to rental_log.txt")

    # Display the log file contents
    try:
        with open("rental_log.txt", "r") as f:
            print("\nCurrent log contents:")
            print(f.read())
    except FileNotFoundError:
        print("Log file not found.")


if __name__ == "__main__":
    main()
