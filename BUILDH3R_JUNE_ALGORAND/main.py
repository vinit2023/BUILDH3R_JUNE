

from algokit_utils.beta.algorand_client import (
    AlgorandClient,
    AssetCreateParams,
    AssetOptInParams,
    AssetTransferParams,
    PayParams,   
)

algorand = AlgorandClient.default_local_net()

dispenser = algorand.account.dispenser()
print("Dispenser Address", dispenser.address)

creator = algorand.account.random()
print("Creator Address:", creator.address)
print(algorand.account.get_information(creator.address))

algorand.send.payment(
    PayParams(
        sender= dispenser.address,
        receiver= creator.address,
        amount= 10_000_000
    )
)

print(algorand.account.get_information(creator.address))

sent_txn = algorand.send.asset_create(
    AssetCreateParams(
        sender=creator.address,
        total=1000,
        asset_name="BUILDH3R",
        unit_name="H3R",
        manager=creator.address,
        clawback=creator.address,
        freeze=creator.address
    )
)


asset_id = sent_txn["confirmation"]["asset-index"]
print("Asset ID",asset_id)


receiver_acc = algorand.account.random()
print("Receiver Address:", receiver_acc.address)


# asset_transfer = algorand.send.asset_transfer(
#     AssetTransferParams(
#         sender=creator.address,
#         receiver=receiver_acc.address,
#         asset_id=asset_id,
#         amount=10
#     )
# )

algorand.send.payment(
    PayParams(
        sender= dispenser.address,
        receiver= receiver_acc.address,
        amount= 10_000_000
    )
)


group_txn = algorand.new_group()

group_txn.add_asset_opt_in(
    AssetOptInParams(
        sender=receiver_acc.address,
        asset_id=asset_id
    )
)

group_txn.add_payment(
    PayParams(
        sender=receiver_acc.address,
        receiver=creator.address,
        amount=1_000_000
    )
)

group_txn.add_asset_transfer(
    AssetTransferParams(
        sender=creator.address,
        receiver=receiver_acc.address,
        asset_id=asset_id,
        amount=500
    )
)

group_txn.execute()

print(algorand.account.get_information(receiver_acc.address))

print("Receiver Account Asset Balance", algorand.account.get_information(receiver_acc.address)['assets'][0]['amount'])
print("Creator Account Asset Balance", algorand.account.get_information(creator.address)['assets'][0]['amount'])


# algorand.send.asset_transfer(
#     AssetTransferParams(
#         sender=creator.address,
#         asset_id=asset_id,
#         clawback_target=receiver_acc.address  ,
#         receiver=receiver_acc.address,
#         amount=1_000_000
#     ) 
# )

# print("Receiver Account Asset Balance", algorand.account.get_information(receiver_acc.address)['assets'][0]['amount'])
# print("Receiver Account Asset Balance", algorand.account.get_information(creator.address)['assets'][0]['amount'])



# Clawback 400 tokens from receiver_acc
clawback_txn = algorand.send.asset_transfer(
    AssetTransferParams(
        sender=creator.address,  # Clawback address
        asset_id=asset_id,
        receiver=creator.address,
        clawback_target=receiver_acc.address,
        amount=400
    )
)

print("After Clawback:")
print("Receiver Account Asset Balance", algorand.account.get_information(receiver_acc.address)['assets'][0]['amount'])
print("Creator Account Asset Balance", algorand.account.get_information(creator.address)['assets'][0]['amount'])