import requests
import time

def test_backend_connection():
    """Test if the backend is running and responding"""
    try:
        response = requests.get("http://localhost:8000/health")
        if response.status_code == 200:
            print("✅ Backend is running and responding")
            return True
        else:
            print("❌ Backend returned unexpected status code:", response.status_code)
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to backend. Is it running?")
        return False
    except Exception as e:
        print("❌ Error connecting to backend:", str(e))
        return False

def test_frontend_connection():
    """Test if the frontend is running and responding"""
    try:
        response = requests.get("http://localhost:3000")
        if response.status_code == 200:
            print("✅ Frontend is running and responding")
            return True
        else:
            print("❌ Frontend returned unexpected status code:", response.status_code)
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to frontend. Is it running?")
        return False
    except Exception as e:
        print("❌ Error connecting to frontend:", str(e))
        return False

def test_api_endpoints():
    """Test some of the API endpoints"""
    try:
        # Test outfit suggestion themes
        response = requests.get("http://localhost:8000/api/v1/outfit-suggestion/themes")
        if response.status_code == 200:
            print("✅ Outfit suggestion themes endpoint working")
        else:
            print("❌ Outfit suggestion themes endpoint failed with status:", response.status_code)
            
        # Test garment generator styles
        response = requests.get("http://localhost:8000/api/v1/garment-generator/styles")
        if response.status_code == 200:
            print("✅ Garment generator styles endpoint working")
        else:
            print("❌ Garment generator styles endpoint failed with status:", response.status_code)
            
        # Test capsule generator themes
        response = requests.get("http://localhost:8000/api/v1/capsule-generator/themes")
        if response.status_code == 200:
            print("✅ Capsule generator themes endpoint working")
        else:
            print("❌ Capsule generator themes endpoint failed with status:", response.status_code)
            
    except Exception as e:
        print("❌ Error testing API endpoints:", str(e))

if __name__ == "__main__":
    print("Testing StyleMate Pro connections...\n")
    
    backend_ok = test_backend_connection()
    frontend_ok = test_frontend_connection()
    
    if backend_ok and frontend_ok:
        print("\n🎉 Both frontend and backend are running!")
        print("\nTesting API endpoints:")
        test_api_endpoints()
    else:
        print("\n⚠️  Please make sure both frontend and backend servers are running.")
        print("   Start them with:")
        print("   - Windows: run start.bat")
        print("   - Mac/Linux: run start.sh")