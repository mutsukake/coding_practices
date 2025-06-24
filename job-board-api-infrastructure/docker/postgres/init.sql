-- PostgreSQL initialization script

-- Create database if not exists
SELECT 'CREATE DATABASE jobboard' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'jobboard')\gexec

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";  -- For better text search performance

-- Create full-text search configuration for job search
CREATE TEXT SEARCH CONFIGURATION IF NOT EXISTS job_search (COPY = english);
