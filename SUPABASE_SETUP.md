# Supabase Setup Guide for Ajan Daily Tracker

## Quick Setup (5 minutes)

### 1. Create Table in Supabase

Go to your Supabase dashboard: https://app.supabase.com

1. Click on **SQL Editor** (left sidebar)
2. Click **New Query**
3. Copy and paste the SQL below, then click **Run**:

```sql
CREATE TABLE tracker_entries (
  id BIGSERIAL PRIMARY KEY,
  device_id TEXT NOT NULL,
  date DATE NOT NULL,
  sleep_6h BOOLEAN DEFAULT FALSE,
  sleep_hours DECIMAL DEFAULT 0,
  bathed BOOLEAN DEFAULT FALSE,
  hair_controlled BOOLEAN DEFAULT FALSE,
  ate_enough BOOLEAN DEFAULT FALSE,
  protein_ok BOOLEAN DEFAULT FALSE,
  dsa_studied BOOLEAN DEFAULT FALSE,
  dsa_hours DECIMAL DEFAULT 0,
  sysdesign_studied BOOLEAN DEFAULT FALSE,
  sysdesign_hours DECIMAL DEFAULT 0,
  deepwork_90min BOOLEAN DEFAULT FALSE,
  solved_designed BOOLEAN DEFAULT FALSE,
  low_distraction BOOLEAN DEFAULT FALSE,
  progress DECIMAL DEFAULT 0,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  UNIQUE(device_id, date)
);

-- Create index for faster queries
CREATE INDEX idx_device_date ON tracker_entries(device_id, date);
```

### 2. Set Up Row Level Security (RLS)

1. Go to **Authentication** → **Policies** (in left sidebar)
2. Click on the `tracker_entries` table
3. Click **New Policy**
4. Choose **Enable read access for all users**
5. Click **Review** → **Save policy**
6. Repeat and choose **Enable insert access for all users**
7. Repeat and choose **Enable update access for all users** (match on `device_id`)

### 3. Done! 🎉

Your tracker will now:
- ✅ Save data to Supabase (cloud)
- ✅ Sync across devices with the same device ID
- ✅ Work offline with localStorage fallback
- ✅ Store data forever (free tier)

### How It Works

- Each device gets a unique ID stored in browser localStorage
- All data is associated with that device ID
- Data syncs automatically to the cloud when you save
- If cloud is down, data saves locally and syncs when back online

### Support

If you need help:
1. Check browser console (F12 → Console) for errors
2. Verify your Supabase credentials in `daily_tracker_web.py`
3. Make sure the `tracker_entries` table exists in your database

---

**That's it! Start tracking your habits now! 🎯**
