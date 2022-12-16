CREATE TABLE `Users` (
  `id` int,
  `username` varchar(255),
  `password` text,
  `create_at` datetime,
  `write_at` datetime
);

CREATE TABLE `Customers` (
  `id` int,
  `user_id` int,
  `first_name` varchar(255),
  `last_name` varchar(255),
  `email` email,
  `address` varchar(255),
  `telephone` int,
  `country_id` int,
  `create_at` datetime,
  `write_at` datetime
);

CREATE TABLE `Countries` (
  `id` int,
  `name` varchar(255),
  `create_at` datetime,
  `write_at` datetime
);

CREATE TABLE `Categories` (
  `id` int,
  `name` varchar(255),
  `description` text,
  `create_at` datetime,
  `write_at` datetime
);

CREATE TABLE `Products` (
  `id` int,
  `name` varchar(255),
  `sku` int,
  `image` image,
  `description` text,
  `price` int,
  `category_id` in,
  `available` boolean,
  `create_at` datetime,
  `write_at` datetime
);

CREATE TABLE `Payment` (
  `id` int,
  `name` varchar(255),
  `allowed` boolean,
  `create_at` datetime,
  `write_at` datetime
);

CREATE TABLE `StatusOrder` (
  `id` int,
  `name` varchar(255),
  `create_at` datetime,
  `write_at` datetime
);

CREATE TABLE `Orders` (
  `id` int,
  `order_number` int,
  `customer_id` int,
  `details` text,
  `grand_total` float,
  `payment_id` int,
  `status_id` int,
  `create_at` datetime,
  `write_at` datetime
);

CREATE TABLE `OrderDetails` (
  `id` int,
  `order_id` int,
  `product_id` int,
  `description_id` text,
  `Quatity` float,
  `price_id` int,
  `discount` float,
  `subtotal` float,
  `total` float,
  `create_at` datetime,
  `write_at` datetime
);

ALTER TABLE `Customers` ADD FOREIGN KEY (`user_id`) REFERENCES `Users` (`id`);

ALTER TABLE `Customers` ADD FOREIGN KEY (`country_id`) REFERENCES `Countries` (`id`);

ALTER TABLE `Products` ADD FOREIGN KEY (`category_id`) REFERENCES `Categories` (`id`);

ALTER TABLE `Orders` ADD FOREIGN KEY (`customer_id`) REFERENCES `Customers` (`id`);

ALTER TABLE `Orders` ADD FOREIGN KEY (`payment_id`) REFERENCES `Payment` (`id`);

ALTER TABLE `Orders` ADD FOREIGN KEY (`status_id`) REFERENCES `StatusOrder` (`id`);

ALTER TABLE `OrderDetails` ADD FOREIGN KEY (`order_id`) REFERENCES `Orders` (`id`);

ALTER TABLE `OrderDetails` ADD FOREIGN KEY (`product_id`) REFERENCES `Products` (`id`);

ALTER TABLE `OrderDetails` ADD FOREIGN KEY (`price_id`) REFERENCES `Products` (`price`);
