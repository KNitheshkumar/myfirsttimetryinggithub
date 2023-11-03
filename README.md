# Custom Django Models and Signals Documentation

This document provides an overview and detailed documentation for the custom Django models and signals used in your project. These models and signals handle user authentication, user profiles, categories, products, orders, and more.

## Custom User Authentication Models

### `CustomUser` Model

The `CustomUser` model extends Django's built-in `AbstractUser` model and adds a `user_type` field for user classification. Users can be categorized as Admin, Staff, Merchant, or Customer.

#### Fields

- **`user_type`** (CharField, max_length=255)
  - Description: Represents the user's role in the application.
  - Choices: Admin (1), Staff (2), Merchant (3), Customer (4).
  - Default: Admin (1)

#### Usage

- Create user accounts with various user types and use this model for user authentication and authorization.

### User Profile Models

#### `AdminUser`, `StaffUser`, `MerchantUser`, `CustomerUser`

These models store profile information for users based on their respective user types. They are linked to the `CustomUser` model, allowing customization of profile data.

#### Fields

- **`profile_pic`** (FileField)
  - Description: Profile picture or image associated with the user.
  - Default: An empty string ("") for optional profile pictures.
  
- **`auth_user_id`** (OneToOneField to `CustomUser`, on_delete=models.CASCADE)
  - Description: Establishes a one-to-one relationship with `CustomUser`.
  - `on_delete`: Specifies behavior when the associated `CustomUser` instance is deleted (CASCADE deletes the profile too).

- **`created_at`** (DateTimeField, auto_now_add=True)
  - Description: Records the creation date and time of the user profile.
  - Default: Automatically generated timestamp upon profile creation.

### Categories and Subcategories Models

#### `Categories` and `SubCategories`

These models are used to categorize products and include fields for titles, URLs, descriptions, and thumbnails. Subcategories are related to categories.

### Products and Related Models

#### `Products`, `ProductMedia`, `ProductTransaction`, `ProductDetails`, `ProductAbout`, `ProductTags`, `ProductQuestions`, `ProductReviews`, `ProductVarient`, `ProductVarientItems`

These models represent products and their associated data, including media, transactions, details, about sections, tags, questions, and reviews. `ProductVarient` and `ProductVarientItems` support product variations.

### Customer Orders Models

#### `CustomerOrders` and `OrderDeliveryStatus`

These models are used to store information about customer orders, including purchase details, discounts, and delivery status.

## Signal Handlers

### Signal to Create User Profiles

- `@receiver(post_save, sender=CustomUser)`
- Function: Create user profiles for different user types when a `CustomUser` instance is created.

### Signal to Save User Profiles

- `@receiver(post_save, sender=CustomUser)`
- Function: Save user profiles when a `CustomUser` instance is updated to ensure profile data is consistent.

## Usage

- Create and manage user accounts with user types.
- Organize products into categories and subcategories.
- Handle product-related data, transactions, details, tags, questions, and reviews.
- Track customer orders and delivery statuses.

## Best Practices

- Maintain consistency in user profile creation and saving based on user types.
- Implement access control and authorization logic tailored to different user roles.

## Security Considerations

- Protect sensitive user data and implement proper access control.
- Securely handle and store profile images and other media.
- Implement secure order processing and protect order-related data.

## Dependencies

- This project is built using Django for user management and data modeling.

## Related Resources

- [Django Documentation](https://docs.djangoproject.com/): Refer to the official Django documentation for more information on models, signals, and authentication.

Feel free to adapt and expand on this documentation as needed for your specific project's requirements.
