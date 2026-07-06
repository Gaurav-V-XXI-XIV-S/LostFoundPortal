CREATE DATABASE IF NOT EXISTS lost_found_portal CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE lost_found_portal;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    email VARCHAR(160) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(30),
    role ENUM('user', 'admin') NOT NULL DEFAULT 'user',
    location VARCHAR(180),
    profile_image VARCHAR(255),
    created_at DATETIME NOT NULL,
    INDEX idx_users_role (role)
);

CREATE TABLE IF NOT EXISTS admin (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL UNIQUE,
    designation VARCHAR(120) DEFAULT 'Portal Administrator',
    permissions JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_admin_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS lost_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    item_name VARCHAR(160) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(80) NOT NULL,
    date_lost DATE NOT NULL,
    location VARCHAR(180) NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    status ENUM('open', 'matched', 'closed') NOT NULL DEFAULT 'open',
    created_at DATETIME NOT NULL,
    CONSTRAINT fk_lost_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_lost_category (category),
    INDEX idx_lost_location (location),
    INDEX idx_lost_date (date_lost)
);

CREATE TABLE IF NOT EXISTS found_items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    item_name VARCHAR(160) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(80) NOT NULL,
    date_found DATE NOT NULL,
    location VARCHAR(180) NOT NULL,
    image_path VARCHAR(255) NOT NULL,
    status ENUM('open', 'claimed', 'closed') NOT NULL DEFAULT 'open',
    created_at DATETIME NOT NULL,
    CONSTRAINT fk_found_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_found_category (category),
    INDEX idx_found_location (location),
    INDEX idx_found_date (date_found)
);

CREATE TABLE IF NOT EXISTS claims (
    id INT AUTO_INCREMENT PRIMARY KEY,
    claimant_id INT NOT NULL,
    lost_item_id INT NOT NULL,
    found_item_id INT NOT NULL,
    similarity_score DECIMAL(5,2) NOT NULL DEFAULT 0,
    message TEXT,
    status ENUM('pending', 'approved', 'rejected') NOT NULL DEFAULT 'pending',
    created_at DATETIME NOT NULL,
    CONSTRAINT fk_claim_user FOREIGN KEY (claimant_id) REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT fk_claim_lost FOREIGN KEY (lost_item_id) REFERENCES lost_items(id) ON DELETE CASCADE,
    CONSTRAINT fk_claim_found FOREIGN KEY (found_item_id) REFERENCES found_items(id) ON DELETE CASCADE,
    UNIQUE KEY uq_claim_pair (claimant_id, lost_item_id, found_item_id),
    INDEX idx_claim_status (status)
);

CREATE TABLE IF NOT EXISTS notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(160) NOT NULL,
    message TEXT NOT NULL,
    is_read BOOLEAN NOT NULL DEFAULT FALSE,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_notification_user FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_notifications_user_read (user_id, is_read)
);
