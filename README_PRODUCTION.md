# ✨ Ajan Daily Tracker

A beautiful, modern web-based daily habit tracker with cloud storage. Track your health, learning, and productivity goals with real-time visualization and cross-device sync.

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

## 🎯 Features

- **💪 Health & Wellness** - Sleep, bathing, nutrition tracking
- **📚 Learning & Growth** - DSA, System Design, problem-solving
- **⚡ Productivity** - Deep work sessions, distraction tracking
- **📊 Real-time Progress** - Live circular progress indicator
- **📅 28-Day History** - Visual heatmap of your performance
- **☁️ Cloud Storage** - Supabase integration for data persistence
- **🔄 Auto-Sync** - Works seamlessly across all devices
- **📱 Responsive Design** - Beautiful UI on desktop and mobile
- **🚀 Fast & Lightweight** - Pure Python backend + modern frontend

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Supabase account (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ajan-daily-tracker.git
   cd ajan-daily-tracker
   ```

2. **Create virtual environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Set up Supabase**
   - Create a new project at [supabase.com](https://supabase.com)
   - Get your project URL and API key
   - Create the `tracker_entries` table (see `SUPABASE_SETUP.md`)
   - Apply RLS policies (see `SUPABASE_POLICIES.sql`)

4. **Update credentials in the code**
   - Open `daily_tracker_web.py`
   - Find the Supabase config section
   - Update with your project URL and API key

5. **Run the application**
   ```bash
   python daily_tracker_web.py
   ```

6. **Open in browser**
   - Visit http://localhost:5000
   - Start tracking! 🎉

## 📋 Project Structure

```
ajan-daily-tracker/
├── daily_tracker_web.py          # Main application
├── .gitignore                    # Git ignore rules
├── README.md                     # This file
├── START_HERE.txt               # Setup guide
├── SUPABASE_SETUP.md            # Supabase configuration
├── SUPABASE_POLICIES.sql        # RLS policies
└── .venv/                       # Virtual environment
```

## 🗄️ Data Storage

Data is stored in **Supabase PostgreSQL** database with the following structure:

```sql
CREATE TABLE tracker_entries (
  id BIGSERIAL PRIMARY KEY,
  device_id TEXT NOT NULL,
  date TEXT NOT NULL,
  sleep_6h BOOLEAN,
  sleep_hours FLOAT,
  bathed BOOLEAN,
  hair_controlled BOOLEAN,
  ate_enough BOOLEAN,
  protein_ok BOOLEAN,
  dsa_studied BOOLEAN,
  dsa_hours FLOAT,
  sysdesign_studied BOOLEAN,
  sysdesign_hours FLOAT,
  deepwork_90min BOOLEAN,
  solved_designed BOOLEAN,
  low_distraction BOOLEAN,
  progress FLOAT,
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(device_id, date)
);
```

## 🔐 Security & Privacy

- **RLS Policies** - Secure device-based access control
- **No Authentication Required** - Uses device ID for identification
- **HTTPS Only** - When deployed to production
- **Data Privacy** - Your data stays in your Supabase project

## 🌐 Deployment

### Deploy on Vercel (Recommended)

1. Push to GitHub
2. Connect to Vercel
3. Configure environment variables
4. Deploy

### Deploy on Render

1. Create Render account
2. Connect GitHub repository
3. Set environment variables
4. Deploy

### Deploy on Railway

1. Create Railway account
2. Connect GitHub
3. Add environment variables
4. Deploy

## 📱 Usage Guide

### Daily Tracking

1. Toggle your habits as you complete them
2. Enter hours for timed activities
3. Watch your progress update in real-time
4. Click "Save Today's Progress"

### Viewing Stats

- **Today's Progress** - Circular progress indicator
- **Quick Stats** - Days tracked, good days, average, streak
- **28-Day History** - Heatmap showing your performance

### Exporting Data

Click "Export Data" to download your data as JSON for backup.

## 🛠️ Tech Stack

- **Backend**: Python (HTTP Server)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Database**: Supabase (PostgreSQL)
- **Hosting**: Local / Cloud (Vercel, Render, Railway)
- **UI**: Modern dark theme with glassmorphism

## 📊 Metrics Tracked

- Sleep ≥ 6 hours
- Hours slept
- Bathed today
- Hair controlled
- Ate enough
- Protein intake OK
- DSA studied
- DSA hours
- System design studied
- System design hours
- Deep work ≥ 90 min
- Solved/designed
- Low distraction day
- Daily progress %

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Support

Need help? Check out:
- `START_HERE.txt` - Setup guide
- `SUPABASE_SETUP.md` - Database configuration
- `SUPABASE_POLICIES.sql` - Security policies

## 🎯 Future Roadmap

- [ ] Mobile app (React Native)
- [ ] Advanced analytics
- [ ] Goal setting
- [ ] Custom habits
- [ ] Social sharing
- [ ] Data visualization charts

---

Made with ❤️ by Ajan Tracker Team

**Start tracking today and become the best version of yourself!** 🚀
