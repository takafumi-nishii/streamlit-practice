import random

def draw_card(deck):
    """山札からカードを1枚引いて返す(山札から削除)"""
    card = random.choice(deck)
    deck.remove(card)
    return card, deck

def judge_round(base_card, result_card, player_choice, bet, chips):
    """1ラウンド分の勝敗判定とチップ増減"""
    if result_card == base_card:
        outcome = "draw"
        # 引き分け → チップ変化なし
    elif player_choice == "High" and result_card > base_card:
        outcome = "win"
        chips += bet
    elif player_choice == "Low" and result_card < base_card:
        outcome = "win"
        chips += bet
    else:
        outcome = "lose"
        chips -= bet
    
    return outcome, chips