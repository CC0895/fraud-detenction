CREATE TABLE merchant (
    merchant_id INT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    merchant_category VARCHAR(255),
    merchant_type VARCHAR(255),
    merchant VARCHAR(255),
    create_time timestamp default current_timestamp with time zone ,
    update_time timestamp
    CONSTRAINT unique_merchant_identifier UNIQUE (merchant_category, merchant_type, merchant)
);


