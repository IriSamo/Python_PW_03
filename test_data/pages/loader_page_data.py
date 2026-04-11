from dataclasses import dataclass


@dataclass(frozen=True)
class LoaderPageData:
    end_point: str
    title: str
    main_header: str


LOADER_PAGE = LoaderPageData(
    end_point="/loader",
    title="Loader",
    main_header="Loader",
)
