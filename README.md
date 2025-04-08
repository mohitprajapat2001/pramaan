# Pramaan: Trust in Every Profile

Pramaan is a ***User Profile as a Service*** built using Django, designed to handle user profiles, personal information, and secure account management. The platform allows users to store and manage essential details like contact information, social media accounts, emergency contacts, subscription plans, and security questions. With built-in phone number validation and support for multiple profile images, Pramaan ensures both a seamless and secure experience for its users.

## Key Features

- **Custom User Authentication**: Built on Django's `AbstractUser`, users can register and log in using their email as the username.
- **User Profile Management**: Users can update their personal information, including their secondary email, phone numbers, date of birth, gender, marital status, and biography.
- **Multiple Profile Images**: Users can manage multiple profile images, with the option to set a primary image.
- **Address Management**: Store multiple addresses with details such as city, region, country, and pincode.
- **Social Media Links**: Manage URLs for popular social media platforms like Facebook, Instagram, LinkedIn, and more.
- **Emergency Contact Information**: Users can add and store emergency contact details, including name, phone number, and relationship to the user.
- **Security Questions**: Users can set up security questions for account recovery.
- **Subscription Plans**: Manage subscription plans with a start and end date, providing an easy way to handle different service tiers.

## Models Overview

### 1. **User**

Extends `AbstractUser` for custom user authentication with email as the primary username.

### 2. **UserDetail**

Stores additional personal information about the user.

- **Fields**:
  - `secondary_email`: User's secondary email address.
  - `phone_number`: User's primary phone number.
  - `secondary_phone_number`: Secondary phone number.
  - `date_of_birth`: Date of birth.
  - `gender`: User's gender.
  - `marital_status`: User's marital status.
  - `bio`: Short biography.

### 3. **Profile**

Stores images for user profiles.

- **Fields**:
  - `image`: Profile image.
  - `primary`: Boolean flag to indicate the primary profile image.

### 4. **Address**

Stores user address details, including city, region, country, and address type.

- **Fields**:
  - `address_line_1`, `address_line_2`: Address details.
  - `city`, `state`, `country`: Foreign keys to `City`, `Region`, and `Country` models from `cities_light`.
  - `pincode`: Postal code.
  - `address_type`: Type of address (home, office, etc.).

### 5. **SocialAccounts**

Stores URLs for social media accounts.

- **Fields**:
  - `facebook`, `instagram`, `twitter`, `linkedin`, `youtube`, `github`, `website`, `tiktok`: Social media URLs.

### 6. **EmergencyDetails**

Stores emergency contact details for the user.

- **Fields**:
  - `name`: Emergency contact name.
  - `phone_number`: Emergency contact phone number.
  - `relationship`: Relationship to the user.

### 7. **SecurityQuestion**

Allows users to set security questions for account recovery.

- **Fields**:
  - `question`: The security question.
  - `answer`: The answer to the security question.

### 8. **Subscription**

Stores information about the user's subscription plan.

- **Fields**:
  - `plan`: Subscription plan type.
  - `start_date`: Subscription start date.
  - `end_date`: Subscription end date (optional).

## Installation

### Prerequisites

- Python 3.x
- Django 3.x or higher
- PostgreSQL (recommended) or another database
- `pip` for package management

## Contributing

Fork the repository.

1. Create a new branch (git checkout -b feature-name).

2. Commit your changes (git commit -am 'Add new feature').

3. Push to your fork (git push origin feature-name).

4. Create a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- `django-phonenumber-field` for phone number validation and formatting.

- `django-cities-light` for the city, region, and country management system.
- `djangorestframework` for building REST APIs.
