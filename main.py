import strategy_deal
import task_io


def main():
    data = task_io.read_task_io_file() 

    data_in_output_file = [] 
    for el in data:
        obj_deal = strategy_deal.StrategyDeal(el) 
        out_list = obj_deal.str()
        for out in out_list:
            data_in_output_file.append(out)

    task_io.write_out_file(data_in_output_file) 


if __name__ == '__main__':
    main()
