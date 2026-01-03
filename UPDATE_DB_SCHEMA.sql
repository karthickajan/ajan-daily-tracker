-- Update Supabase Database Schema
-- Remove device_id column and fix constraints

-- Step 1: Drop the old unique constraint that included device_id
ALTER TABLE tracker_entries DROP CONSTRAINT IF EXISTS tracker_entries_device_id_date_key;

-- Step 2: Add unique constraint on date only
ALTER TABLE tracker_entries ADD CONSTRAINT tracker_entries_date_key UNIQUE(date);

-- Step 3: Drop device_id column
ALTER TABLE tracker_entries DROP COLUMN IF EXISTS device_id;

-- Step 4: Verify the table structure
SELECT column_name, data_type, is_nullable 
FROM information_schema.columns 
WHERE table_name = 'tracker_entries' 
ORDER BY ordinal_position;

-- Now all your data will sync across all devices!
