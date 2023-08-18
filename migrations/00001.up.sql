-- Active: 1692299907002@@127.0.0.1@5432@tech_stack_db
CREATE TABLE IF NOT EXISTS users(
        id UUID PRIMARY KEY,
        name VARCHAR(32) NOT NULL,
        fullname VARCHAR(64) DEFAULT NULL,
        created_at TIMESTAMP WITH TIME ZONE NOT NULL,
        updated_at TIMESTAMP WITH TIME ZONE NOT NULL,
        deleted_at TIMESTAMP DEFAULT NULL
    );
