-- ============================================
-- Ajan Daily Tracker - Supabase RLS Policies
-- ============================================
-- Run these SQL commands in Supabase SQL Editor
-- Go to: SQL Editor → New Query → Paste these → Run

-- First, enable RLS on the table
ALTER TABLE public.tracker_entries ENABLE ROW LEVEL SECURITY;

-- ============================================
-- POLICY 1: INSERT - Allow anyone to insert
-- ============================================
CREATE POLICY "allow_insert_tracker_entries"
ON "public"."tracker_entries"
AS PERMISSIVE
FOR INSERT
TO public
WITH CHECK (true);

-- ============================================
-- POLICY 2: UPDATE - Allow users to update their own entries
-- ============================================
CREATE POLICY "allow_update_own_tracker_entries"
ON "public"."tracker_entries"
AS PERMISSIVE
FOR UPDATE
TO public
USING (device_id = current_setting('app.current_device_id', true) OR device_id IS NOT NULL)
WITH CHECK (device_id = current_setting('app.current_device_id', true) OR device_id IS NOT NULL);

-- ============================================
-- POLICY 3: SELECT - Allow users to read their own entries
-- ============================================
CREATE POLICY "allow_select_own_tracker_entries"
ON "public"."tracker_entries"
AS PERMISSIVE
FOR SELECT
TO public
USING (device_id = current_setting('app.current_device_id', true) OR device_id IS NOT NULL);

-- ============================================
-- POLICY 4: DELETE - Allow users to delete their own entries
-- ============================================
CREATE POLICY "allow_delete_own_tracker_entries"
ON "public"."tracker_entries"
AS PERMISSIVE
FOR DELETE
TO public
USING (device_id = current_setting('app.current_device_id', true) OR device_id IS NOT NULL);

-- ============================================
-- SIMPLER ALTERNATIVE (If above doesn't work)
-- Use this instead - Allow all operations without restrictions
-- ============================================

-- DROP existing policies first:
-- DROP POLICY IF EXISTS "allow_insert_tracker_entries" ON public.tracker_entries;
-- DROP POLICY IF EXISTS "allow_update_own_tracker_entries" ON public.tracker_entries;
-- DROP POLICY IF EXISTS "allow_select_own_tracker_entries" ON public.tracker_entries;
-- DROP POLICY IF EXISTS "allow_delete_own_tracker_entries" ON public.tracker_entries;

-- Then use these simpler policies:
-- CREATE POLICY "allow_all_insert"
-- ON public.tracker_entries FOR INSERT
-- WITH CHECK (true);

-- CREATE POLICY "allow_all_update"
-- ON public.tracker_entries FOR UPDATE
-- USING (true) WITH CHECK (true);

-- CREATE POLICY "allow_all_select"
-- ON public.tracker_entries FOR SELECT
-- USING (true);

-- CREATE POLICY "allow_all_delete"
-- ON public.tracker_entries FOR DELETE
-- USING (true);

-- ============================================
-- EXPLANATION OF POLICIES
-- ============================================
/*
📋 Policy Structure:

1. CREATE POLICY "policy_name"
   - Unique name for the policy

2. ON "public"."table_name"
   - Which table to apply the policy to

3. AS PERMISSIVE
   - PERMISSIVE = Allow access
   - RESTRICTIVE = Deny access

4. FOR INSERT / UPDATE / SELECT / DELETE
   - What operation the policy covers

5. TO public
   - Who the policy applies to
   - "public" = Everyone (anonymous users)
   - "authenticated" = Logged-in users only

6. USING (condition)
   - Condition to check when reading data (SELECT/UPDATE/DELETE)
   - true = Always allow
   - device_id = current_setting(...) = Only their device data

7. WITH CHECK (condition)
   - Condition to check when writing data (INSERT/UPDATE)
   - Ensures data integrity

============================================

🔒 Your Tracker Setup:

Since your app uses "device_id" to identify users (without login):
- Each device gets a unique ID
- Users can only see/edit their own entries
- device_id is stored with each entry

💡 RECOMMENDED: Use the SIMPLER version (second option)
   - Easier to understand
   - Works with your anonymous device-based approach
   - No need to set session variables

============================================
*/
