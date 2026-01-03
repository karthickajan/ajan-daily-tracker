# WSGI configuration for PythonAnywhere
# This file serves your Ajan Daily Tracker

import sys
import os

# Add your project to Python path
path = '/home/karthickajan/mysite'
if path not in sys.path:
    sys.path.append(path)

# Load the HTML template and database functions from your tracker
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>✨ Ajan Daily Tracker</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-dark: #0f0f1a;
            --bg-card: #1a1a2e;
            --bg-card-hover: #252542;
            --bg-input: #16213e;
            --accent: #e94560;
            --accent-glow: rgba(233, 69, 96, 0.3);
            --success: #00d9a0;
            --success-glow: rgba(0, 217, 160, 0.3);
            --warning: #ffc048;
            --warning-glow: rgba(255, 192, 72, 0.3);
            --text-primary: #ffffff;
            --text-secondary: #8b8ba7;
            --border: #2a2a4a;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: var(--bg-dark);
            color: var(--text-primary);
            min-height: 100vh;
            background-image: 
                radial-gradient(ellipse at 10% 20%, rgba(233, 69, 96, 0.08) 0%, transparent 50%),
                radial-gradient(ellipse at 90% 80%, rgba(0, 217, 160, 0.08) 0%, transparent 50%);
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        /* Header */
        .header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 2.5rem;
            flex-wrap: wrap;
            gap: 1.5rem;
        }

        .header-left h1 {
            font-size: 2.5rem;
            font-weight: 800;
            background: linear-gradient(135deg, #fff 0%, #a0a0c0 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 0.5rem;
        }

        .header-left p {
            color: var(--text-secondary);
            font-size: 1rem;
        }

        .date-badge {
            background: var(--bg-card);
            padding: 1rem 1.5rem;
            border-radius: 1rem;
            text-align: center;
            border: 1px solid var(--border);
            backdrop-filter: blur(10px);
        }

        .date-badge .day {
            font-size: 1.25rem;
            font-weight: 700;
            color: var(--accent);
        }

        .date-badge .date {
            color: var(--text-secondary);
            font-size: 0.9rem;
            margin-top: 0.25rem;
        }

        /* Main Grid */
        .main-grid {
            display: grid;
            grid-template-columns: 1fr 320px;
            gap: 1.5rem;
        }

        @media (max-width: 900px) {
            .main-grid {
                grid-template-columns: 1fr;
            }
        }

        /* Cards */
        .card {
            background: var(--bg-card);
            border-radius: 1.25rem;
            padding: 1.5rem;
            border: 1px solid var(--border);
            margin-bottom: 1.5rem;
            transition: all 0.3s ease;
        }

        .card:hover {
            background: var(--bg-card-hover);
            border-color: rgba(255, 255, 255, 0.1);
            transform: translateY(-2px);
        }

        .card-title {
            font-size: 1.25rem;
            font-weight: 700;
            margin-bottom: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        .card-title .icon {
            font-size: 1.5rem;
        }

        /* Toggle Items */
        .toggle-item {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.875rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }

        .toggle-item:last-child {
            border-bottom: none;
        }

        .toggle-label {
            font-size: 0.95rem;
            color: var(--text-primary);
        }

        .toggle-right {
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }

        /* Custom Toggle Switch */
        .toggle-switch {
            position: relative;
            width: 52px;
            height: 28px;
        }

        .toggle-switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }

        .toggle-slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: var(--border);
            border-radius: 34px;
            transition: all 0.3s ease;
        }

        .toggle-slider:before {
            position: absolute;
            content: "";
            height: 22px;
            width: 22px;
            left: 3px;
            bottom: 3px;
            background: white;
            border-radius: 50%;
            transition: all 0.3s ease;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }

        .toggle-switch input:checked + .toggle-slider {
            background: var(--success);
            box-shadow: 0 0 20px var(--success-glow);
        }

        .toggle-switch input:checked + .toggle-slider:before {
            transform: translateX(24px);
        }

        /* Hour Input */
        .hour-input {
            width: 60px;
            padding: 0.5rem;
            background: var(--bg-input);
            border: 1px solid var(--border);
            border-radius: 0.5rem;
            color: var(--text-primary);
            font-size: 0.9rem;
            text-align: center;
            transition: all 0.3s ease;
        }

        .hour-input:focus {
            outline: none;
            border-color: var(--accent);
            box-shadow: 0 0 15px var(--accent-glow);
        }

        .hour-label {
            color: var(--text-secondary);
            font-size: 0.8rem;
        }

        /* Stats Panel */
        .stats-panel {
            position: sticky;
            top: 2rem;
        }

        /* Circular Progress */
        .progress-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 1.5rem 0;
        }

        .circular-progress {
            position: relative;
            width: 160px;
            height: 160px;
        }

        .circular-progress svg {
            transform: rotate(-90deg);
        }

        .circular-progress circle {
            fill: none;
            stroke-width: 10;
        }

        .progress-bg {
            stroke: var(--border);
        }

        .progress-bar {
            stroke: var(--success);
            stroke-linecap: round;
            transition: stroke-dashoffset 0.5s ease, stroke 0.3s ease;
        }

        .progress-text {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            text-align: center;
        }

        .progress-text .value {
            font-size: 2.5rem;
            font-weight: 800;
        }

        .progress-text .label {
            color: var(--text-secondary);
            font-size: 0.9rem;
        }

        .status-message {
            text-align: center;
            margin-top: 1rem;
            font-size: 1.1rem;
            font-weight: 600;
        }

        /* Quick Stats */
        .stat-row {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.75rem 0;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        }

        .stat-row:last-child {
            border-bottom: none;
        }

        .stat-label {
            color: var(--text-secondary);
            font-size: 0.9rem;
        }

        .stat-value {
            font-weight: 700;
            color: var(--success);
        }

        /* Buttons */
        .button-group {
            display: flex;
            gap: 1rem;
            margin-top: 1.5rem;
            flex-wrap: wrap;
        }

        .btn {
            padding: 1rem 2rem;
            border: none;
            border-radius: 0.75rem;
            font-size: 1rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .btn-primary {
            background: var(--accent);
            color: white;
            flex: 1;
        }

        .btn-primary:hover {
            background: #ff6b7a;
            box-shadow: 0 0 30px var(--accent-glow);
            transform: translateY(-2px);
        }

        .btn-secondary {
            background: var(--bg-input);
            color: var(--text-primary);
            border: 1px solid var(--border);
        }

        .btn-secondary:hover {
            background: var(--border);
        }

        /* Toast Notification */
        .toast {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            background: var(--success);
            color: white;
            padding: 1rem 1.5rem;
            border-radius: 0.75rem;
            font-weight: 600;
            box-shadow: 0 10px 40px rgba(0, 217, 160, 0.3);
            transform: translateY(100px);
            opacity: 0;
            transition: all 0.3s ease;
            z-index: 1000;
        }

        .toast.show {
            transform: translateY(0);
            opacity: 1;
        }

        /* History Section */
        .history-card {
            margin-top: 1.5rem;
        }

        .history-grid {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 0.5rem;
            margin-top: 1rem;
        }

        .history-day {
            aspect-ratio: 1;
            border-radius: 0.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.75rem;
            font-weight: 600;
            cursor: default;
            transition: all 0.2s ease;
        }

        .history-day.empty {
            background: var(--border);
            opacity: 0.3;
        }

        .history-day.low {
            background: var(--accent);
            opacity: 0.7;
        }

        .history-day.medium {
            background: var(--warning);
        }

        .history-day.high {
            background: var(--success);
        }

        .history-day:hover {
            transform: scale(1.1);
        }

        /* Responsive */
        @media (max-width: 600px) {
            .container {
                padding: 1rem;
            }
            
            .header-left h1 {
                font-size: 1.75rem;
            }
            
            .button-group {
                flex-direction: column;
            }
            
            .btn {
                justify-content: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <header class="header">
            <div class="header-left">
                <h1>Ajan Daily Tracker</h1>
                <p>Track your daily habits and become the best version of yourself</p>
            </div>
            <div class="date-badge">
                <div class="day" id="current-day">Saturday</div>
                <div class="date" id="current-date">03 January 2026</div>
            </div>
        </header>

        <!-- Main Grid -->
        <div class="main-grid">
            <!-- Left Column - Trackers -->
            <div class="trackers-column">
                <!-- Health & Wellness -->
                <div class="card">
                    <h2 class="card-title"><span class="icon">💪</span> Health & Wellness</h2>
                    
                    <div class="toggle-item">
                        <span class="toggle-label">Sleep ≥ 6 hours</span>
                        <div class="toggle-right">
                            <input type="number" class="hour-input" id="sleep_hours" min="0" max="24" step="0.5" value="0">
                            <span class="hour-label">hrs</span>
                            <label class="toggle-switch">
                                <input type="checkbox" id="sleep_6h" onchange="updateProgress()">
                                <span class="toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                    
                    <div class="toggle-item">
                        <span class="toggle-label">Bathed Today</span>
                        <div class="toggle-right">
                            <label class="toggle-switch">
                                <input type="checkbox" id="bathed" onchange="updateProgress()">
                                <span class="toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                    
                    <div class="toggle-item">
                        <span class="toggle-label">Hair Controlled</span>
                        <div class="toggle-right">
                            <label class="toggle-switch">
                                <input type="checkbox" id="hair_controlled" onchange="updateProgress()">
                                <span class="toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                    
                    <div class="toggle-item">
                        <span class="toggle-label">Ate Enough</span>
                        <div class="toggle-right">
                            <label class="toggle-switch">
                                <input type="checkbox" id="ate_enough" onchange="updateProgress()">
                                <span class="toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                    
                    <div class="toggle-item">
                        <span class="toggle-label">Protein Intake OK</span>
                        <div class="toggle-right">
                            <label class="toggle-switch">
                                <input type="checkbox" id="protein_ok" onchange="updateProgress()">
                                <span class="toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                </div>

                <!-- Learning & Growth -->
                <div class="card">
                    <h2 class="card-title"><span class="icon">📚</span> Learning & Growth</h2>
                    
                    <div class="toggle-item">
                        <span class="toggle-label">DSA Studied</span>
                        <div class="toggle-right">
                            <input type="number" class="hour-input" id="dsa_hours" min="0" max="24" step="0.5" value="0">
                            <span class="hour-label">hrs</span>
                            <label class="toggle-switch">
                                <input type="checkbox" id="dsa_studied" onchange="updateProgress()">
                                <span class="toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                    
                    <div class="toggle-item">
                        <span class="toggle-label">System Design Studied</span>
                        <div class="toggle-right">
                            <input type="number" class="hour-input" id="sysdesign_hours" min="0" max="24" step="0.5" value="0">
                            <span class="hour-label">hrs</span>
                            <label class="toggle-switch">
                                <input type="checkbox" id="sysdesign_studied" onchange="updateProgress()">
                                <span class="toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                    
                    <div class="toggle-item">
                        <span class="toggle-label">Solved Problem / Designed</span>
                        <div class="toggle-right">
                            <label class="toggle-switch">
                                <input type="checkbox" id="solved_designed" onchange="updateProgress()">
                                <span class="toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                </div>

                <!-- Productivity -->
                <div class="card">
                    <h2 class="card-title"><span class="icon">⚡</span> Productivity</h2>
                    
                    <div class="toggle-item">
                        <span class="toggle-label">Deep Work ≥ 90 min</span>
                        <div class="toggle-right">
                            <label class="toggle-switch">
                                <input type="checkbox" id="deepwork_90min" onchange="updateProgress()">
                                <span class="toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                    
                    <div class="toggle-item">
                        <span class="toggle-label">Low Distraction Day</span>
                        <div class="toggle-right">
                            <label class="toggle-switch">
                                <input type="checkbox" id="low_distraction" onchange="updateProgress()">
                                <span class="toggle-slider"></span>
                            </label>
                        </div>
                    </div>
                </div>

                <!-- Buttons -->
                <div class="button-group">
                    <button class="btn btn-primary" onclick="saveEntry()">
                        💾 Save Today's Progress
                    </button>
                    <button class="btn btn-secondary" onclick="exportData()">
                        📤 Export Data
                    </button>
                </div>

                <!-- History -->
                <div class="card history-card">
                    <h2 class="card-title"><span class="icon">📅</span> Last 28 Days</h2>
                    <div class="history-grid" id="history-grid">
                        <!-- Filled by JS -->
                    </div>
                </div>
            </div>

            <!-- Right Column - Stats -->
            <div class="stats-panel">
                <div class="card">
                    <h2 class="card-title"><span class="icon">📊</span> Today's Progress</h2>
                    
                    <div class="progress-container">
                        <div class="circular-progress">
                            <svg width="160" height="160">
                                <circle class="progress-bg" cx="80" cy="80" r="70"></circle>
                                <circle class="progress-bar" id="progress-circle" cx="80" cy="80" r="70"
                                    stroke-dasharray="439.8" stroke-dashoffset="439.8"></circle>
                            </svg>
                            <div class="progress-text">
                                <div class="value" id="progress-value">0%</div>
                                <div class="label">Complete</div>
                            </div>
                        </div>
                        <div class="status-message" id="status-message">Let's get started! ✨</div>
                    </div>
                </div>

                <div class="card">
                    <h2 class="card-title"><span class="icon">📈</span> Quick Stats</h2>
                    
                    <div class="stat-row">
                        <span class="stat-label">Total Days Tracked</span>
                        <span class="stat-value" id="total-days">0</span>
                    </div>
                    
                    <div class="stat-row">
                        <span class="stat-label">Days ≥ 80%</span>
                        <span class="stat-value" id="good-days">0</span>
                    </div>
                    
                    <div class="stat-row">
                        <span class="stat-label">Average Progress</span>
                        <span class="stat-value" id="avg-progress">0%</span>
                    </div>
                    
                    <div class="stat-row">
                        <span class="stat-label">Current Streak 🔥</span>
                        <span class="stat-value" id="streak">0 days</span>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Toast -->
    <div class="toast" id="toast">✅ Saved successfully!</div>

    <script>
        // Supabase Configuration
        const SUPABASE_URL = 'https://suxszrvczmdfajekqyrw.supabase.co';
        const SUPABASE_API_KEY = 'sb_publishable_PAqRM1mxu_St436Be0NwVw_Aj7MW-kp';
        
        // Data storage
        let trackerData = {entries: []};
        let userId = null;
        let isLoading = true;
        
        const toggleKeys = ['sleep_6h', 'bathed', 'hair_controlled', 'ate_enough', 'protein_ok', 
                           'dsa_studied', 'sysdesign_studied', 'deepwork_90min', 'solved_designed', 'low_distraction'];
        const hourKeys = ['sleep_hours', 'dsa_hours', 'sysdesign_hours'];

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            updateDate();
            initializeApp();
        });

        function updateDate() {
            const now = new Date();
            const days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'];
            const months = ['January', 'February', 'March', 'April', 'May', 'June', 
                          'July', 'August', 'September', 'October', 'November', 'December'];
            
            document.getElementById('current-day').textContent = days[now.getDay()];
            document.getElementById('current-date').textContent = 
                `${String(now.getDate()).padStart(2, '0')} ${months[now.getMonth()]} ${now.getFullYear()}`;
        }

        function initializeApp() {
            // Use fixed device ID for this personal tracker
            userId = 'ajan_user';
            
            // Load from localStorage and Supabase
            loadData();
        }

        function loadData() {
            const saved = localStorage.getItem('ajanTrackerData');
            if (saved) {
                trackerData = JSON.parse(saved);
            }
            
            // Fetch all data from Supabase for this device (async)
            fetchFromSupabase().then(() => {
                // Update UI after fetch completes
                const today = new Date().toISOString().split('T')[0];
                const todayEntry = trackerData.entries.find(e => e.date === today);
                
                if (todayEntry) {
                    toggleKeys.forEach(key => {
                        const el = document.getElementById(key);
                        if (el) el.checked = todayEntry[key] || false;
                    });
                    hourKeys.forEach(key => {
                        const el = document.getElementById(key);
                        if (el) el.value = todayEntry[key] || 0;
                    });
                }
                
                updateProgress();
                updateStats();
                renderHistory();
            });
        }

        function fetchFromSupabase() {
            return new Promise((resolve) => {
                console.log('Fetching all entries from Supabase');
                
                // Fetch ALL entries from Supabase (no device_id filter)
                fetch(`${SUPABASE_URL}/rest/v1/tracker_entries?order=date.desc`, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        'apikey': SUPABASE_API_KEY,
                        'Authorization': `Bearer ${SUPABASE_API_KEY}`
                    }
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Supabase response:', data);
                    if (data && data.length > 0) {
                        console.log('Found', data.length, 'entries from Supabase');
                        // Replace all entries with Supabase data
                        trackerData.entries = data.map(row => ({
                            date: row.date,
                            sleep_6h: row.sleep_6h,
                            sleep_hours: row.sleep_hours,
                            bathed: row.bathed,
                            hair_controlled: row.hair_controlled,
                            ate_enough: row.ate_enough,
                            protein_ok: row.protein_ok,
                            dsa_studied: row.dsa_studied,
                            dsa_hours: row.dsa_hours,
                            sysdesign_studied: row.sysdesign_studied,
                            sysdesign_hours: row.sysdesign_hours,
                            deepwork_90min: row.deepwork_90min,
                            solved_designed: row.solved_designed,
                            low_distraction: row.low_distraction,
                            progress: row.progress
                        }));
                        // Save synced data to localStorage
                        localStorage.setItem('ajanTrackerData', JSON.stringify(trackerData));
                        console.log('✅ Synced', trackerData.entries.length, 'entries to localStorage');
                    } else {
                        console.log('No entries found in Supabase');
                    }
                    resolve();
                })
                .catch(e => {
                    console.error('Error fetching from Supabase:', e);
                    resolve();
                });
            });
        }

        function saveData() {
            localStorage.setItem('ajanTrackerData', JSON.stringify(trackerData));
            
            // Try to sync with Supabase
            syncWithSupabase();
        }

        function syncWithSupabase() {
            const today = new Date().toISOString().split('T')[0];
            const todayEntry = trackerData.entries.find(e => e.date === today);
            
            if (!todayEntry) return;
            
            // Prepare data for Supabase
            const data = {
                date: today,
                sleep_6h: todayEntry.sleep_6h,
                sleep_hours: todayEntry.sleep_hours,
                bathed: todayEntry.bathed,
                hair_controlled: todayEntry.hair_controlled,
                ate_enough: todayEntry.ate_enough,
                protein_ok: todayEntry.protein_ok,
                dsa_studied: todayEntry.dsa_studied,
                dsa_hours: todayEntry.dsa_hours,
                sysdesign_studied: todayEntry.sysdesign_studied,
                sysdesign_hours: todayEntry.sysdesign_hours,
                deepwork_90min: todayEntry.deepwork_90min,
                solved_designed: todayEntry.solved_designed,
                low_distraction: todayEntry.low_distraction,
                progress: todayEntry.progress
            };
            
            // First, check if entry exists for today
            fetch(`${SUPABASE_URL}/rest/v1/tracker_entries?date=eq.${today}`, {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'apikey': SUPABASE_API_KEY,
                    'Authorization': `Bearer ${SUPABASE_API_KEY}`
                }
            })
            .then(response => response.json())
            .then(existingData => {
                if (existingData && existingData.length > 0) {
                    // UPDATE existing entry
                    console.log('Updating existing entry for', today);
                    const entryId = existingData[0].id;
                    
                    fetch(`${SUPABASE_URL}/rest/v1/tracker_entries?id=eq.${entryId}`, {
                        method: 'PATCH',
                        headers: {
                            'Content-Type': 'application/json',
                            'apikey': SUPABASE_API_KEY,
                            'Authorization': `Bearer ${SUPABASE_API_KEY}`
                        },
                        body: JSON.stringify(data)
                    })
                    .then(response => {
                        if (response.ok) {
                            console.log('✅ Updated in Supabase');
                        } else {
                            console.error('Failed to update in Supabase');
                        }
                    })
                    .catch(e => console.error('Update error:', e));
                } else {
                    // INSERT new entry
                    console.log('Creating new entry for', today);
                    
                    fetch(`${SUPABASE_URL}/rest/v1/tracker_entries`, {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json',
                            'apikey': SUPABASE_API_KEY,
                            'Authorization': `Bearer ${SUPABASE_API_KEY}`
                        },
                        body: JSON.stringify(data)
                    })
                    .then(response => {
                        if (response.ok) {
                            console.log('✅ Saved to Supabase');
                        } else {
                            console.error('Failed to save to Supabase');
                        }
                    })
                    .catch(e => console.error('Insert error:', e));
                }
            })
            .catch(e => console.error('Error checking existing entry:', e));
        }

        function calculateProgress() {
            let completed = 0;
            toggleKeys.forEach(key => {
                if (document.getElementById(key).checked) completed++;
            });
            return (completed / toggleKeys.length) * 100;
        }

        function updateProgress() {
            const progress = calculateProgress();
            const circle = document.getElementById('progress-circle');
            const circumference = 2 * Math.PI * 70;
            const offset = circumference - (progress / 100) * circumference;
            
            circle.style.strokeDashoffset = offset;
            
            if (progress >= 80) {
                circle.style.stroke = '#00d9a0';
            } else if (progress >= 50) {
                circle.style.stroke = '#ffc048';
            } else {
                circle.style.stroke = '#e94560';
            }
            
            document.getElementById('progress-value').textContent = Math.round(progress) + '%';
            
            const statusEl = document.getElementById('status-message');
            if (progress >= 100) {
                statusEl.textContent = "Perfect day! 🏆";
                statusEl.style.color = '#00d9a0';
            } else if (progress >= 80) {
                statusEl.textContent = "Excellent work! 🌟";
                statusEl.style.color = '#00d9a0';
            } else if (progress >= 60) {
                statusEl.textContent = "Good progress! 💪";
                statusEl.style.color = '#ffc048';
            } else if (progress >= 40) {
                statusEl.textContent = "Keep pushing! 🚀";
                statusEl.style.color = '#ffc048';
            } else {
                statusEl.textContent = "Let's get started! ✨";
                statusEl.style.color = '#e94560';
            }
        }

        function saveEntry() {
            const today = new Date().toISOString().split('T')[0];
            const entry = { date: today, progress: calculateProgress() };
            
            toggleKeys.forEach(key => {
                entry[key] = document.getElementById(key).checked;
            });
            hourKeys.forEach(key => {
                entry[key] = parseFloat(document.getElementById(key).value) || 0;
            });
            
            const existingIndex = trackerData.entries.findIndex(e => e.date === today);
            if (existingIndex >= 0) {
                trackerData.entries[existingIndex] = entry;
            } else {
                trackerData.entries.push(entry);
            }
            
            saveData();
            updateStats();
            renderHistory();
            showToast("✅ Progress saved successfully!");
        }

        function updateStats() {
            const entries = trackerData.entries;
            const totalDays = entries.length;
            const goodDays = entries.filter(e => (e.progress || 0) >= 80).length;
            const avgProgress = totalDays > 0 
                ? entries.reduce((sum, e) => sum + (e.progress || 0), 0) / totalDays 
                : 0;
            
            document.getElementById('total-days').textContent = totalDays;
            document.getElementById('good-days').textContent = goodDays;
            document.getElementById('avg-progress').textContent = avgProgress.toFixed(1) + '%';
            document.getElementById('streak').textContent = calculateStreak() + ' days';
        }

        function calculateStreak() {
            if (trackerData.entries.length === 0) return 0;
            
            const sorted = [...trackerData.entries].sort((a, b) => b.date.localeCompare(a.date));
            let streak = 0;
            
            for (const entry of sorted) {
                if ((entry.progress || 0) >= 80) {
                    streak++;
                } else {
                    break;
                }
            }
            
            return streak;
        }

        function renderHistory() {
            const grid = document.getElementById('history-grid');
            grid.innerHTML = '';
            
            const today = new Date();
            const entries = trackerData.entries;
            
            for (let i = 27; i >= 0; i--) {
                const d = new Date(today);
                d.setDate(d.getDate() - i);
                const dateStr = d.toISOString().split('T')[0];
                const entry = entries.find(e => e.date === dateStr);
                
                const div = document.createElement('div');
                div.className = 'history-day';
                
                if (entry) {
                    const progress = entry.progress || 0;
                    if (progress >= 80) {
                        div.className += ' high';
                    } else if (progress >= 50) {
                        div.className += ' medium';
                    } else {
                        div.className += ' low';
                    }
                    div.textContent = d.getDate();
                    div.title = `${dateStr}: ${Math.round(progress)}%`;
                } else {
                    div.className += ' empty';
                    div.textContent = d.getDate();
                }
                
                grid.appendChild(div);
            }
        }

        function showToast(message) {
            const toast = document.getElementById('toast');
            toast.textContent = message;
            toast.classList.add('show');
            setTimeout(() => toast.classList.remove('show'), 3000);
        }

        function exportData() {
            const dataStr = JSON.stringify(trackerData, null, 2);
            const blob = new Blob([dataStr], {type: 'application/json'});
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'ajan_tracker_data.json';
            a.click();
            URL.revokeObjectURL(url);
            showToast("📤 Data exported successfully!");
        }
    </script>
</body>
</html>
'''

# WSGI Application
def application(environ, start_response):
    """
    Simple WSGI application that serves your Ajan Daily Tracker
    """
    path = environ.get('PATH_INFO', '/')
    method = environ.get('REQUEST_METHOD', 'GET')
    
    if path == '/' or path == '/index.html':
        # Serve the HTML
        status = '200 OK'
        headers = [('Content-type', 'text/html; charset=utf-8')]
        start_response(status, headers)
        return [HTML_TEMPLATE.encode('utf-8')]
    else:
        # 404 for other paths
        status = '404 Not Found'
        headers = [('Content-type', 'text/plain')]
        start_response(status, headers)
        return [b'Not Found']
