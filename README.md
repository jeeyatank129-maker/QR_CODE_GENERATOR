# ✨ **Universal QR Pro** - Desktop QR Code Generator

A **professional desktop application** built with **Python Tkinter** for generating **custom QR codes** with multi-format support and logo overlay functionality.

## 🚀 **Features**

| Feature | Description |
|---------|-------------|
| **📱 3 QR Formats** | Link/Text, Wi-Fi Network, Contact (vCard) |
| **🖼️ Logo Overlay** | Add custom PNG/JPG logos to QR center |
| **🔒 Wi-Fi Toggle** | Show/hide password with eye icon functionality |
| **📏 Auto-sizing** | QR expands automatically for complex data |
| **👁️ Live Preview** | 250x250px preview before saving |
| **💾 Direct Save** | PNG export with file dialog |
| **🔄 Smart Refresh** | One-click reset all fields |
| **✅ Error Handling** | Input validation + logo error recovery |

## 🧰 **Tech Stack**
Frontend: Python Tkinter, ttk themed widgets, PIL
QR Engine: qrcode[pil] + Pillow
Data Formats: WIFI:, vCard 3.0, plain text/URL
File I/O: PIL Image processing


## 🛠️ **Sample Usage Scenarios**

| QR Type | Input Format | Scanned Result |
|---------|--------------|----------------|
| **Wi-Fi** | `MyWiFi`, `password123` | Auto-connects to WiFi |
| **vCard** | `John Doe;+919876543210;john@email.com` | Saves contact |
| **Link** | `https://rajkotbusiness.com` | Opens website |
| **Text** | `Call me at 9876543210` | Plain text display |

## 📱 **UI/UX Design**



📱 UI/UX Design
┌──────────────────────────────┐
│  Select QR Type: [Dropdown]  │  ← Dynamic form switching
│                              │
│  📝 Input Fields             │  ← Context-aware inputs
│  • WiFi: SSID + Password     │
│  • vCard: Name;Phone;Email   │
│                              │
│  ☐ Add logo [📁 Browse]     │  ← Optional logo overlay
│                              │
│  [GENERATE] [REFRESH]        │  ← Action buttons
│                              │
│  ┌─────────────────────┐     │
│  │  [QR PREVIEW]       │     │  ← Live 250x250 preview
│  │  Your QR appears    │     │
│  └─────────────────────┘     │
└──────────────────────────────┘

Universal-QR-Pro/
│
├── qr_app.py       # Main GUI application
├── QR_LOGIC.py     # QR generation logic
└── README.md       # This file

## 🚀 **Quick Setup**

```bash
# Clone repository
git clone <your-repo-url>
cd Universal-QR-Pro

# Install dependencies
pip install qrcode[pil] pillow

# Run application
python qr_app.py


💯 Production-ready desktop app! No internet required, perfect for offline use in shops, restaurants, and small businesses. 
 Combines power of qrcode library with professional Tkinter UX! 🎉
