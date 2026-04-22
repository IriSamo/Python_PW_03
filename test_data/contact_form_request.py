positive_requests_data = [
    # Standard valid data
    (
        "John",
        "Smith",
        "john.smith@example.com",
        "Hello! This is a valid contact form message."
    ),

    # Valid data with special characters in name
    (
        "Anna-Marie",
        "O'Connor",
        "anna.oconnor@example.com",
        "Requesting additional information about your services."
    ),
]


negative_requests_data = [
    # Invalid email format
    (
        "Mike",
        "Taylor",
        "mike.taylor@invalid",
        "Testing invalid email validation."
    ),

    # Empty required message field
    (
        "Sara",
        "Wilson",
        "sara.wilson@example.com",
        ""
    ),
]