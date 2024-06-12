## Summary of what I learnt

ZKSync is an ultra-fast ZK protocol that is EVM compatible, allowing smart contracts to be written in Solidity or Vyper and compiled using zksolc, zkSync's default compiler.

Through this process, I gained proficiency in setting up Solidity projects on Remix, activating plugins, deploying contracts, and making calls to them via Remix. My first hands-on experience was with the Zeek Messages contract. This contract features a sendMessage function that accepts and stores messages. Upon deployment, it emits a single event and includes functions to retrieve the last message and the total number of messages.

Next, I delved into the ERC20 token contract, learning how to import and create contracts from OpenZeppelin and the process of token creation. I successfully deployed these contracts and interacted with them directly from Remix, with all transactions verifiable on the explorer.

Additionally, I discovered how to interact with deployed contracts using scripts and blockchain libraries such as Ethers.js, broadening the scope of interaction beyond the Remix environment.


message sender deployed at: https://sepolia.explorer.zksync.io/address/0x5a8d317dCdDe2A53E5474f862493c3C6F9C75E40

token contract: https://sepolia.explorer.zksync.io/address/0x89eb38cD07093980B5D91837d4790c3d03eE1006

