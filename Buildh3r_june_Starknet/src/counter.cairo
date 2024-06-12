#[starknet::contract]
mod Counter{

    #[storage]
    struct Storage {
        num: u128,
    }

    #[constructor]
    fn constructor(ref self: ContractState) {}

    #[external(v0)]
    fn increase_counter(ref self: ContractState) {
        self.num.write(self.num.read() + 1 );
    }

    #[external(v0)]
    fn decrease_counter(ref self: ContractState) {
        self.num.write(self.num.read() - 1 );
    }

    #[external(v0)]
    fn get_count(self: @ContractState) -> u128 {
        self.num.read()
    }
}