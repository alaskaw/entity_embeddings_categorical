from entity_embeddings import Config, Embedder, TargetType
from entity_embeddings.util import visualization_utils


def main():
    data_path = "../processed_rossmann.csv"
    config = Config.make_default_config(csv_path=data_path,
                                        target_name='Sales',
                                        target_type=TargetType.REGRESSION,
                                        train_ratio=0.9,
                                        epochs=20,
                                        verbose=True,
                                        artifacts_path='artifacts')

    embedder = Embedder(config)
    embedder.perform_embedding()

    visualization_utils.make_visualizations_from_config(config, extension='png')


if __name__ == '__main__':
    main()
