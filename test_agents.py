# File: test_agents.py
import test

def calculate_promo(inventory, competitor_discount, baseline_margin, min_margin_floor, budget):
    proposed_discount = competitor_discount + 2.0
    net_margin = baseline_margin - proposed_discount
    
    if net_margin < min_margin_floor:
        max_allowed_discount = baseline_margin - min_margin_floor
        return max_allowed_discount, "Capped by Financial Overseer"
        
    return proposed_discount, "Approved by All Agents"

def test_festive_clearance_approval():
    discount, status = calculate_promo(1500, 15.0, 40.0, 15.0, 500000)
    assert discount == 17.0
    assert status == "Approved by All Agents"

def test_diwali_margin_shield_activation():
    discount, status = calculate_promo(2500, 35.0, 40.0, 15.0, 500000)
    assert discount == 25.0
    assert status == "Capped by Financial Overseer"
