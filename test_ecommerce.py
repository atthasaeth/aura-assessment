import re
from playwright.sync_api import Page, expect
import pytest

# --- Configuration ---
# ในงานจริงค่าเหล่านี้ควรอยู่ใน Environment Variables หรือ Config file
BASE_URL = "https://www.saucedemo.com"
USERNAME = "standard_user"
PASSWORD = "secret_sauce"

@pytest.fixture(scope="function", autouse=True)
def setup(page: Page):
    """
    Fixture นี้จะทำงานก่อนทุก Test Case
    ช่วยประหยัดเวลาในการเขียน URL ซ้ำๆ
    """
    page.goto(BASE_URL)

def test_login_success(page: Page):
    """
    Test Case 1: ทดสอบการ Login (Mandatory Flow)
    """
    # 1. Fill Username & Password using User-Facing Locators
    # ใช้ get_by_placeholder เพื่อความเสถียรมากกว่า CSS Selector ทั่วไป
    page.get_by_placeholder("Username").fill(USERNAME)
    page.get_by_placeholder("Password").fill(PASSWORD)
    
    # 2. Click Login
    page.get_by_role("button", name="Login").click()
    
    # 3. Assertions (ตรวจสอบผลลัพธ์)
    # เช็คว่า URL เปลี่ยนไปหน้า Inventory
    expect(page).to_have_url(re.compile(".*inventory.html"))
    # เช็คว่ามีหัวข้อ "Products" แสดงขึ้นมา
    expect(page.get_by_text("Products")).to_be_visible()

def test_add_to_cart_and_verify(page: Page):
    """
    Test Case 2: ค้นหาของ -> ใส่ตะกร้า -> ตรวจสอบตะกร้า (Mandatory Flow)
    """
    # --- Pre-condition: ต้อง Login ก่อน ---
    page.get_by_placeholder("Username").fill(USERNAME)
    page.get_by_placeholder("Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()

    # --- Step 1: Find Item & Add to Cart ---
    # สมมติว่าเราจะซื้อ "Sauce Labs Backpack"
    product_name = "Sauce Labs Backpack"
    
    # หา Product Card ที่มีชื่อนี้ แล้วกดปุ่ม Add to cart ภายใน Card นั้น
    # เทคนิคนี้ช่วยให้มั่นใจว่ากดปุ่มของสินค้าถูกชิ้นแน่นอน
    page.locator(".inventory_item") \
        .filter(has_text=product_name) \
        .get_by_role("button", name="Add to cart") \
        .click()

    # --- Step 2: Verify Cart Badge (UI Feedback) ---
    # ตรวจสอบว่ามีเลข '1' ขึ้นที่ไอคอนรถเข็น
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    # --- Step 3: Go to Cart Page & Verify Data ---
    page.locator(".shopping_cart_link").click()
    
    # เช็คว่า URL คือหน้า Cart
    expect(page).to_have_url(re.compile(".*cart.html"))
    
    # เช็คว่าสินค้าในตะกร้า ชื่อตรงกับที่เรากดซื้อ (Data Integrity)
    cart_item = page.locator(".inventory_item_name")
    expect(cart_item).to_have_text(product_name)
    
    # (Optional) เช็คราคา
    expect(page.locator(".inventory_item_price")).to_be_visible()