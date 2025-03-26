CREATE TABLE IF NOT EXISTS merchant (
    merchant_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    merchant_category VARCHAR(255),
    merchant_type VARCHAR(255),
    merchant VARCHAR(255),
    create_time TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
    update_time TIMESTAMPTZ,
    CONSTRAINT unique_merchant_identifier UNIQUE (merchant_category, merchant_type, merchant)
);
