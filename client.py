from typing import Dict, Any, List

class UpsellCrossSellClient:
    def get_offers(self, current_cart_skus: List[str]) -> Dict[str, Any]:
        rules = {
            "phone": {"upsell": "phone_pro_max", "cross_sell": ["case", "screen_protector"]},
            "laptop": {"upsell": "laptop_16inch", "cross_sell": ["docking_station", "mouse"]},
            "headphones": {"upsell": "headphones_anc", "cross_sell": ["carrying_case"]}
        }
        offers = []
        for sku in current_cart_skus:
            if sku in rules:
                offers.append({
                    "sku": sku,
                    "upsell_recommendation": rules[sku]["upsell"],
                    "cross_sell_recommendations": rules[sku]["cross_sell"]
                })
        return {"recommendations": offers}
