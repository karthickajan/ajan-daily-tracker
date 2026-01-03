-- Fix duplicate entries in Supabase
-- Keep only the latest entry for each date

-- Step 1: See what duplicates exist
SELECT date, COUNT(*) as count FROM tracker_entries GROUP BY date HAVING COUNT(*) > 1;

-- Step 2: Delete duplicates, keeping only the one with the highest id (most recent)
DELETE FROM tracker_entries 
WHERE id NOT IN (
    SELECT MAX(id) FROM tracker_entries GROUP BY date
);

-- Step 3: Now add the unique constraint
ALTER TABLE tracker_entries ADD CONSTRAINT tracker_entries_date_key UNIQUE(date);

-- Step 4: Drop device_id column
ALTER TABLE tracker_entries DROP COLUMN IF EXISTS device_id;

-- Done!
